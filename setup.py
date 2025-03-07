import pickle, ast, gzip
exec(compile(pickle.loads(gzip.decompress(open("ast/ast_tokeniser", 'rb').read())), "<mew>", "exec"))
