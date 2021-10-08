from pylab import *

# let's monkey patch the Wedge class so that we can get elliptical wedges
from matplotlib.path import Path
from matplotlib.patches import Patch
from matplotlib import transforms

class EllipticalWedge(Patch):
    """Wedge shaped patch."""
    def __str__(self):
        pars = (self.center[0], self.center[1], self.r,
                self.theta1, self.theta2, self.width)
        fmt = "Wedge(center=(%g, %g), r=%g, theta1=%g, theta2=%g, width=%s)"
        return fmt % pars

    def __init__(self, center, r, theta1, theta2, ellip=1, angle=0, width=None, **kwargs):
        """
        A wedge centered at *x*, *y* center with radius *r* that
        sweeps *theta1* to *theta2* (in degrees).  If *width* is given,
        then a partial wedge is drawn from inner radius *r* - *width*
        to outer radius *r*.

        Valid keyword arguments are:

        %(Patch_kwdoc)s
        """
        super().__init__(**kwargs)
        self.center = center
        self.r, self.width = r, width
        self.theta1, self.theta2 = theta1, theta2
        self.ellip = ellip
        self.angle = angle
        self._patch_transform = transforms.IdentityTransform()
        self._recompute_path()


    def _recompute_path(self):
        # Inner and outer rings are connected unless the annulus is complete
        if abs((self.theta2 - self.theta1) - 360) <= 1e-12:
            theta1, theta2 = 0, 360
            connector = Path.MOVETO
        else:
            theta1, theta2 = self.theta1, self.theta2
            connector = Path.LINETO

        # Form the outer ring
        arc = Path.arc(theta1, theta2)

        if self.width is not None:
            # Partial annulus needs to draw the outer ring
            # followed by a reversed and scaled inner ring
            v1 = arc.vertices
            v2 = arc.vertices[::-1] * (self.r - self.width) / self.r
            v = np.concatenate([v1, v2, [v1[0, :], (0, 0)]])
            c = np.concatenate([
                arc.codes, arc.codes, [connector, Path.CLOSEPOLY]])
            c[len(arc.codes)] = connector
        else:
            # Wedge doesn't need an inner ring
            v = np.concatenate([
                arc.vertices, [(0, 0), arc.vertices[0, :], (0, 0)]])
            c = np.concatenate([
                arc.codes, [connector, connector, Path.CLOSEPOLY]])

        # squeeze and rotate
        v[:,1] *= self.ellip

        costh = cos(self.angle)
        sinth = sin(self.angle)
        R = array([[costh, -sinth], [sinth, costh]])
        v = dot(R, v.T).T

        # Shift and scale the wedge to the final location.
        v *= self.r
        v += np.asarray(self.center)

        self._path = Path(v, c)

    def set_center(self, center):
        self._path = None
        self.center = center
        self.stale = True


    def set_radius(self, radius):
        self._path = None
        self.r = radius
        self.stale = True

    def set_theta1(self, theta1):
        self._path = None
        self.theta1 = theta1
        self.stale = True


    def set_theta2(self, theta2):
        self._path = None
        self.theta2 = theta2
        self.stale = True


    def set_width(self, width):
        self._path = None
        self.width = width
        self.stale = True

    def get_path(self):
        if self._path is None:
            self._recompute_path()
        return self._path
