# _*_ coding: utf-8 _*_
# @Time      18-8-6 下午12:01
# @File      CSRT_train.py
# @Software  PyCharm
# @Author    JK.Rao

from libs.network.factory import get_network
from libs.crafting_table.factory import train_model

# network = get_network('CSTR')
# loss_dict = network.structure_loss()
# opti = network.define_optimizer(loss_dict)
train_model('CSTR')
a = 1
