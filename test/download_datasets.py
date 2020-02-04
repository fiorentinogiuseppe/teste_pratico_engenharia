import wget

with open('../datasets/datasets.txt', 'r') as f:
    datasets = f.readlines()

for dataset in datasets:
    url = dataset.split('\n')[0]
    out_path = '../datasets/' + url.rsplit("/",1)[1]
    filename = wget.download(url, out=out_path)
