from ssg import hooks, parsers


files = []


@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: not isinstance(p, parsers.ResourceParser)
    for parser in list(filter(valid, site_parsers)):
            if parser.valid_file_ext