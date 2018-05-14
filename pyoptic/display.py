import matplotlib.pyplot as plt
import numpy as np


def plot2d(rays, sli='xz'):
    if sli == 'xz':
        def plot_ray(ray):
            ra = np.array([ri.p0 for ri in ray])
            if not ray[-1].p1 == None:
                ra = np.vstack([ra, ray[-1].p1])
            plt.plot(ra[:, 2], ra[:, 0], c=ray[0].color)
    
    if sli == 'zx':
        def plot_ray(ray):
            ra = np.array([ri.p0 for ri in ray])
            if not ray[-1].p1 == None:
                ra = np.vstack([ra, ray[-1].p1])
            plt.plot(ra[:, 0], ra[:, 2], c=ray[0].color)
    
    if sli == 'xy':
        def plot_ray(ray):
            ra = np.array([ri.p0 for ri in ray])
            plt.plot(ra[:, 1], ra[:, 0], c=ray[0].color)
    
    for ray in rays:
        plot_ray(ray)


def plot_system2d(sys, sli='xz'):
    if sli == 'xz':
        def plot_surf(s):
            sf = s.surface(proj='y')
            plt.plot(sf[2], sf[0], 'k')
    
    if sli == 'zx':
        def plot_surf(s):
            sf = s.surface(proj='y')
            plt.plot(sf[0], sf[2], 'k')
    
    if sli == 'xy':
        def plot_surf(s):
            sf = s.surface(proj='z')
            plt.plot(sf[1], sf[0], 'k')
    
    for s in sys:
        plot_surf(s)


def dotplt(rays):
    NA = max([np.sin(np.arccos(np.dot(r_[-1].d, rays[0][-1].d))) for r_ in rays[1:]])
    r_dl = rays[0][-1].wavelength * 1e-6 / (2 * NA)
    pts = np.array([r_i[-1].p0 for r_i in rays])
    plt.plot(pts[:, 1] - pts[:, 1].mean(), pts[:, 0] - pts[:, 0].mean(), '.')
    
    t = np.linspace(0, 2 * np.pi)
    plt.plot(r_dl * np.sin(t), r_dl * np.cos(t))
    plt.axis('equal')
    #xlim(-.06, .06)
    plt.ylim(-r_dl*3, r_dl*3)