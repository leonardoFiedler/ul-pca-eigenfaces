from argparse import ArgumentParser
import cv2 as cv
import numpy as np
import os
from person import Person
import random
import sys

START_COMPS = 10
MAX_COMPS = 21

TRAIN_SIZE = 7 #70% para treino e 30% para teste

def get_file_contents(file_name, dataset_path):
    """Obtem o conteudo do arquivo

    Args:
        file_name (string): nome do arquivo
        dataset_path (string): caminho da pasta do dataset

    Returns:
        [array(float64)]: Retorna o array com float64 com a imagem em escala 
        de cinza e redimensionada a 80x80
    """
    
    # leitura da imagem
    img = cv.imread(os.path.join(dataset_path, file_name), cv.IMREAD_GRAYSCALE)
    
    # Redimensionamento para 80x80
    img_resized = cv.resize(img, (80, 80))
    
    # Conversao para vetor coluna
    img_resized.T.reshape(1, img_resized.shape[0] * img_resized.shape[1])
    
    # Converte para Float 64
    return np.float64(img_resized)

def file_to_person(file_name, dataset_path):
    """Converte um nome de arquivo para um objeto do tipo Pessoa

    Args:
        file_name (string): nome do arquivo
        dataset_path (string): caminho da pasta do dataset

    Returns:
        [Person]: Pessoa criada apos a conversao
    """
    
    name, _ = os.path.splitext(file_name)
    data = name.split("_")
    
    id = int(data[0])
    label = int(data[1])
    data = get_file_contents(file_name, dataset_path)
    
    return Person(id, label, data)

def load_dataset(path, train_size=7, samples_per_person=10):
    """Efetua o carregamento do dataset

    Args:
        path (string): caminho da pasta do dataset
        train_size (int, optional): Valor correspondente ao tamanho do treino (Padrao corresponde a 70%). Defaults to 7.
        samples_per_person (int, optional): Quantidade de exemplares por pessoa. Defaults to 10.

    Returns:
        [list, list]: Listas contendo as pessoas separadas em treino e teste
    """
    file_names = [fn for fn in os.listdir(path) if fn.endswith('.jpg')]
    
    print(f'Tamanho Total do Dataset: {len(file_names)}')
    
    lst_people = []
    
    for file_name in file_names:
        lst_people.append(file_to_person(file_name, path))
    
    lst_people.sort(key=lambda x: x.id)
    
    samples = []
    
    train, test = [], []
    
    for person in lst_people:
        samples.append(person)
        
        if len(samples) == samples_per_person:
            while len(samples) > train_size:
                index = random.randint(0, len(samples) - 1)
                test.append(samples.pop(index))
            
            if train_size == samples_per_person:
                test.extend(samples)
            
            train.extend(samples)
            samples.clear()
    
    print(f'Tamanho do Dataset de Treino: {len(train)}')
    print(f'Tamanho do Dataset de Teste: {len(test)}')
    return train, test

def load_args():
    """Carregamento dos argumentos

    Returns:
        [ArgumentParser]: Argumentos carregados
    """
    parser = ArgumentParser()

    parser.add_argument(
        '-d', 
        '--dataset', 
        type=str,
        default='./ORL',
        help='Caminho para as imagens do dataset')
    
    return parser

def main(args):
    train, test = load_dataset(args.dataset)
    
    for num_component in range(START_COMPS, MAX_COMPS):
        model = cv.face.EigenFaceRecognizer_create(num_component)
        
        X_train = []
        y_train = []
        
        for item in train:
            X_train.append(item.data)
            y_train.append(item.label)

        model.train(X_train, np.array(y_train))

        corrects = 0
        min_distance = sys.float_info.min
        max_distance = sys.float_info.min
        mean_distance = 0
        
        for test_item in test:
            test_data = test_item.data
            
            label, confidence = model.predict(test_data)
            
            if label == test_item.label:
                corrects += 1
            
            if confidence < min_distance:
                min_distance = confidence
            
            if confidence > max_distance:
                max_distance = confidence
            
            mean_distance += confidence
        
        accuracy = corrects / len(test) * 100
        print(corrects)
        print(f'{num_component} componentes principais, acurácia: {accuracy:.2f}%')
        print('*' * 80)
                

# Programa principal
if __name__ == "__main__":
    parser = load_args()
    args = parser.parse_args()
    main(args)

