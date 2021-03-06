#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import json
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn import kernel_ridge
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn import svm
from expr_utils import filter_by_ranges, expr, load_dataset
from sklearn.gaussian_process import GaussianProcess


def linear():
    regr = linear_model.LinearRegression()
    expr(regr,  "linear", feat, cnt)


def ridge():
    regr = linear_model.Ridge(alpha=0.001)
    expr(regr, "ridge", feat, cnt)


def lkridge():
    regr = kernel_ridge.KernelRidge(alpha=0.00001)
    expr(regr,  "linear kernel ridge regression", feat, cnt)


def lksvr():
    scaler = StandardScaler()
    regr = svm.LinearSVR(C=35)
    pipeline = Pipeline([('scaler', scaler), ('svr', regr)])
    expr(pipeline,  "linear kernel SVR", feat, cnt)


def rbfsvr():
    scaler = StandardScaler()
    regr = svm.SVR(C=4e3, gamma=0.0003)
    pipeline = Pipeline([('scaler', scaler), ('svr', regr)])
    expr(pipeline,  "rbf kernel SVR", feat, cnt)


def gpr():
    scaler = StandardScaler()
    regr = GaussianProcess(regr='linear', corr='linear', theta0=0.3)
    pipeline = Pipeline([('scaler', scaler), ('gpr', regr)])
    expr(pipeline,  "GPR", feat, cnt)


def main():
    # print feat_train.shape, feat_test.shape
    linear()
    # ridge()
    # # lkridge()
    # lksvr()
    # rbfsvr()
    # gpr()

if __name__ == '__main__':
    with open('config.json') as cfg_file:
        cfg = json.load(cfg_file)['mall']

    feat1, cnt = load_dataset(cfg['cvt_feat1'])
    feat, cnt = load_dataset(cfg['cvt_feat'])
    print feat.shape
    feat_segm = feat[:, :10]
    feat_edge = feat[:, 10:17]
    feat_fast = feat1[:, [15]]
    feat_glcm = feat[:, 26:]
    feat = np.c_[feat_segm, feat_edge, feat_glcm, feat_fast]
    # plt.plot(feat_fast, cnt, '.')
    # plt.show()
    # feat = feat[:, 17:29]
    main()
