import yaml
import os

curPath = os.path.dirname(os.path.realpath(__file__))
ymPath = os.path.join(curPath, "t3.yaml")

f = open(ymPath, "r", encoding='utf-8')
cfg = f.read()
f.close()

print(type(cfg))
print(cfg)

a = yaml.load(cfg)
print(a)
print(type(a))