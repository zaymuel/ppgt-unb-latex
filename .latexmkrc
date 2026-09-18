# Multiplatform configuration (Windows / Linux / macOS) for latexmk
# Compiles nomenclature list (.nlo -> .nls)

add_cus_dep('nlo', 'nls', 0, 'makenlo2nls');
sub makenlo2nls {
    my ($base_name) = @_;
    return system("makeindex \"$base_name.nlo\" -s nomencl.ist -o \"$base_name.nls\"");
}
push @generated_exts, 'nlo', 'nls';

