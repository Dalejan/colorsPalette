from sklearn.cluster import KMeans
from js import document
from pyodide import create_proxy

def clustering(imageArray):
    n_clusters = int(document.getElementById("n_clusters").value)
    cluster = KMeans(n_clusters = n_clusters)
    cluster.fit(imageArray)

    #Cluster centroids values (center of cluster)
    centroids=cluster.cluster_centers_
    return centroids

def generatePalette(image):
    '''
    We require an RGB pixel intensity to cluster. If the image contains MXN pixels then the shape of the image is (M, N,3) so we are reshaping image array to shape (M*N,3).
    '''
    imageData=image.reshape((image.shape[1]*image.shape[0],3))
    paletteRGBValues = clustering(imageData)
    return paletteRGBValues



def showPaletteDOM(*ags, **kwgs ):
    #Not necesary to import loadFile.py thanks to pyscript env paths :D
    rgbPalette = generatePalette(localImage.imageData)
    paleteContainer = document.getElementById("palette-container")
    # Clear the previous palette
    paleteContainer.innerHTML = ""

    for rgbColor in rgbPalette:

        color = document.createElement('div')
        paragraph = document.createElement('p')

        color.style.backgroundColor = 'rgb(' + ','.join(str(x) for x in rgbColor) + ')'
        paragraph.innerHTML = color.style.backgroundColor

        color.appendChild(paragraph)
        paleteContainer.appendChild(color)
