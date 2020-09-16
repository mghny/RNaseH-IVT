let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  buildInputs = [
    pkgs.python37
    pkgs.python37Packages.biopython
  ];
}
