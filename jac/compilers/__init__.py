compilers = {}


class CompilerMeta(type):
    def __new__(meta, name, bases, attrs):
        cls = type.__new__(meta, name, bases, attrs)
        for m in attrs['supported_mimetypes']:
            if m in compilers:
                raise RuntimeError('For now, just one compiler by mimetype')
            compilers[m] = cls

        return cls


def compile(what, mimetype):
    """
    Compile a given text based on mimetype.
    """

    try:
        compiler = compilers[mimetype.lower()]
    except KeyError:
        raise RuntimeError('Compiler for mimetype %s not found.' % mimetype)

    return compiler.compile(what)


from .sass import SassCompiler
