# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import glob
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """






    def decompress_zip(path_zip, extract_to):
        with zipfile.ZipFile(path_zip, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    def make_output_dir(output_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def create_dataset(input_folder, output_file):
        dataset = []
        sentiments = ['negative', 'neutral', 'positive'] 

        for sentiment in sentiments:
            sentiment_folder = os.path.join(input_folder, sentiment)
            for file_path in glob.glob(os.path.join(sentiment_folder, '*')):
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read().strip()
                    dataset.append([text, sentiment])

        df = pd.DataFrame(dataset, columns=['phrase', 'target'])
        df.to_csv(output_file, index=False)

        return df

    input_zip = 'files/input.zip'
    extract_to = 'files'
    decompress_zip(input_zip, extract_to)

    output_dir = 'files/output'
    make_output_dir(output_dir)

    train_df = create_dataset(os.path.join(extract_to, 'input/train'), os.path.join(output_dir, 'train_dataset.csv'))
    test_df = create_dataset(os.path.join(extract_to, 'input/test'), os.path.join(output_dir, 'test_dataset.csv'))

    train_df, test_df