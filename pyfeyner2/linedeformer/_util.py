import pyx


def _clean_intersections(paths, intersections, epsilon=0.01):
    output = []
    for path, params in zip(paths, intersections):
        if (abs(pyx.unit.tocm(path.paramtoarclen(params[0]))) < epsilon
            or abs(pyx.unit.tocm(path.arclen()) - pyx.unit.tocm(path.paramtoarclen(params[0]))) < epsilon):
            params = params[1:]
        if (abs(pyx.unit.tocm(path.paramtoarclen(params[-1]))) < epsilon
            or abs(pyx.unit.tocm(path.arclen()) - pyx.unit.tocm(path.paramtoarclen(params[-1]))) < epsilon):
            params = params[:-1]
        output.append(params)
    return output


def _deform_two_paths(paths, mirror, is3d, skip3d, parity3d):
    if mirror:
        paths = paths[::-1]
    if not is3d:
        return paths

    path_intersections = paths[0].intersect(paths[1])
    path_intersections = _clean_intersections(paths, path_intersections)

    output = []
    for path, intersections, parity in zip(paths, path_intersections, [True, False]):
        params = []
        if parity3d == 0:
            parity = not parity
        for intersection in intersections:
            if parity:
                params.append(intersection - skip3d)
                params.append(intersection + skip3d)
            parity = not parity
        pathbits = path.split(params)
        on = True
        for pathbit in pathbits:
            if on:
                output.append(pathbit)
            on = not on
    return output


def _clean_cuts(path, intersections, epsilon=0.01):
    return _clean_intersections([path], [intersections], epsilon)[0]
