import torch
import torch.nn as nn


class Softmax(nn.Module):

    def __init__(self, dim=-1):
        super(Softmax, self).__init__()
        self.dim = dim

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=self.dim, keepdim=True)


class SoftmaxStable(nn.Module):
    def __init__(self, dim=-1):
        super(SoftmaxStable, self).__init__()
        self.dim = dim

    def forward(self, x):
        return torch.exp(x - torch.max(x, dim=self.dim, keepdim=True)[0]) / torch.sum(
            torch.exp(x - torch.max(x, dim=self.dim, keepdim=True)[0]), dim=self.dim, keepdim=True)


def calculate_softmax(data, stable=False):
    if stable:
        softmax = SoftmaxStable()
    else:
        softmax = Softmax()

    output = softmax(data)
    return output


def main():
    while True:
        try:
            input_str = input("Enter Tensor: ")
            if input_str.lower() == 'q':
                break

            data_list = [float(x) for x in input_str.split()]

            data = torch.tensor(data_list)

            output = calculate_softmax(data)
            print(f"Softmax output: {output}")

            output_stable = calculate_softmax(data, stable=True)
            print(f"SoftmaxStable output: {output_stable}")

        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập các số phân cách bởi dấu cách.")


if __name__ == "__main__":
    main()