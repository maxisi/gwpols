# Parametrizing gravitational-wave polarizations

[![Build paper](https://github.com/maxisi/gwpols/actions/workflows/paper-maker.yml/badge.svg)](https://github.com/maxisi/gwpols/actions/workflows/paper-maker.yml) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7016057.svg)](https://doi.org/10.5281/zenodo.7016057)
[![Latest PDF](https://img.shields.io/badge/PDF-latest-orange.svg?style=flat)](https://github.com/maxisi/gwpols/blob/main-pdf/polpars.pdf)
[![arXiv](https://img.shields.io/badge/arXiv-2208.03372-crimson)](https://arxiv.org/abs/2208.03372)

Code and additional material related to the paper on _Parametrizing gravitational-wave polarizations_ (Isi 2022, [arXiv:2208.03372](https://arxiv.org/abs/2208.03372)). The paper reviews the formalism of gravitational wave (GW) polarizations as it pertains practical data analysis applications, and derives a variety of useful parameterizations and corresponding Jacobians.

Python code used to produce most of the figures in the paper can be found in the `notebooks/` directory; the remaining plots were produced using [TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) based on the Tex files in `fig/`. Additionally, many of the calculations presented in the paper are carried out explicitly in the `etc/jacobians.nb` Mathematica notebook.

:point_right: Check out a short web summary of polarization basics [here](https://maxisi.github.io/gwpols/) (with animations!)

If you find any of this useful, please cite the above [DOI](https://doi.org/10.5281/zenodo.7016057) for the code, and the paper:

```
@article{Isi:2022mbx,
    author = "Isi, Maximiliano",
    title = "{Parametrizing gravitational-wave polarizations}",
    eprint = "2208.03372",
    archivePrefix = "arXiv",
    primaryClass = "gr-qc",
    reportNumber = "LIGO-P2200221",
    month = "8",
    year = "2022"
}
```
