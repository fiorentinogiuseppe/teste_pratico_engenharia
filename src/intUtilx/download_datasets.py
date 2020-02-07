import wget


def load_datases(path_file_name='../../datasets/datasets.txt'):
    """
    Load file containing dataset's name
    Parameters
    ----------
    path_file_name: str
        File with datasets name

    Returns
    -------
    None
    """
    with open(path_file_name, 'r') as f:
        datasets = f.readlines()
    return datasets


for dataset in load_datases():
    url = dataset.split('\n')[0]
    out_path = '../datasets/' + url.rsplit("/",1)[1]
    filename = wget.download(url, out=out_path)
