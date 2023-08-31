import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, linear_model, svm) # Mission #2 and #3) You need to import some modules if necessary
from matplotlib.lines import Line2D # For the custom legend

def load_wdbc_data(filename):
    class WDBCData:
        data = []
        target = []
        target_names = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()
    # TODO
    wdbc.data = np.array(wdbc.data)
    return wdbc

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()
    #wdbc = load_wdbc_data('wdbc.data') # Mission #1) Implement 'load_wdbc_data()'

    # Train a model
    model1 = linear_model.SGDClassifier(learning_rate='constant',eta0=0.001)                       # Mission #2) Try at least two different classifiers
    model1.fit(wdbc.data, wdbc.target)
    model2 = linear_model.RidgeClassifier(alpha=1.0)                       # Mission #2) Try at least two different classifiers
    model2.fit(wdbc.data, wdbc.target)

    # Test the model
    predict1 = model1.predict(wdbc.data)
    predict2 = model2.predict(wdbc.data)
    n_correct1 = sum(predict1 == wdbc.target)
    n_correct2 = sum(predict2 == wdbc.target)
    accuracy1 = n_correct1 / len(wdbc.data)
    accuracy2 = n_correct2 / len(wdbc.data)
    balanced_accuracy1 = 0.5 * n_correct1 / len(wdbc.data)
    balanced_accuracy2 = 0.5 * n_correct2 / len(wdbc.data)
    
    # Visualize testing results
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(0, 1)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.subplot(2,1,1)
        plt.title(f'linear_model/SGD ({n_correct1}/{len(wdbc.data)}={accuracy1:.3f})({balanced_accuracy1:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predict1])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
        plt.show()
    for (x, y) in [(0, 1)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.subplot(2,1,2)
        plt.title(f'linear_model/Ridge ({n_correct2}/{len(wdbc.data)}={accuracy2:.3f})({balanced_accuracy2:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predict2])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
        plt.show()
