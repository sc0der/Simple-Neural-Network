from network import Network

net = Network(10, 5, 5)
net.run([1, 0.5,0.1, 0.2, 0.7, 0.9, 1, 0.6, 0.3, 0.1])
out = net.output()
print(out)