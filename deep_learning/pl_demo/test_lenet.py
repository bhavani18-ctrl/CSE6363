import sys
import torch
from torch import nn
from torchvision import transforms
from torchvision.datasets import CIFAR10
import pytorch_lightning as pl

from LeNetModel import LeNetModel


def main(args):
    # Prepare the dataset

    model = LeNetModel.load_from_checkpoint(
        checkpoint_path=args[1]
    )

    test_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))
    ])

    trainer = pl.Trainer()
    trainer.test(model, dataloaders=torch.utils.data.DataLoader(CIFAR10("~/Data/CIFAR10/", train=False, download=True, transform=test_transforms), batch_size=256, num_workers=12, shuffle=False))


if __name__ == "__main__":
    main(sys.argv)
