# Assignment 4 — Generative Models and Neural Architecture Search

This assignment explores probabilistic generative modeling, adversarial learning, and automated neural-network architecture design. The three notebooks use MNIST as the principal image dataset.

## 1. Variational Autoencoders

Notebook: `01_variational_autoencoders.ipynb`

- Basic Variational Autoencoder architecture and training.
- Latent-space visualization and exploration.
- β-VAE and the reconstruction/KL-divergence trade-off.
- Disentangled representations and latent traversal.
- Conditional VAE (CVAE) and conditional interpolation.
- VAE-based anomaly detection and reconstruction-error visualization.

## 2. Generative Adversarial Networks

Notebook: `02_generative_adversarial_networks.ipynb`

- DCGAN generator, discriminator, and adversarial training loop.
- Training dynamics and mode-collapse analysis.
- Wasserstein GAN with weight clipping.
- WGAN-GP and gradient penalty.
- Conditional GAN and latent/class interpolation.
- Quantitative evaluation with Inception Score and Fréchet Inception Distance.
- Spectral normalization and AdaIN/StyleGAN-related concepts.

## 3. Neural Architecture Search

Notebook: `03_neural_architecture_search.ipynb`

- CNN search-space representation and architecture-to-model construction.
- Random-search baseline.
- Architecture mutation and evolutionary search.
- Simplified differentiable architecture search (DARTS).
- Comparison of search methods.
- Multi-objective and progressive architecture-search extensions.

## Main tools

Python, PyTorch, torchvision, NumPy, Pandas, Matplotlib, Seaborn, SciPy, scikit-learn, and tqdm.

## Data

The notebooks use `torchvision.datasets.MNIST` with `download=True`. MNIST is therefore downloaded automatically into the local `data/` directory when the relevant cells are run. Downloaded MNIST files and generated image archives are not included in this repository.

## Run

From this assignment directory:

```bash
pip install -r ../../requirements/assignment-04.txt
jupyter lab
```

GPU acceleration is optional. On CPU, training may take longer; adjust epochs and batch sizes only if you clearly document the change when reporting results.
