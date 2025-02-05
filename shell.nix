{ pkgs ? import <nixpkgs> { config.allowUnfree = true; } }:

pkgs.mkShell {
  packages = [
    pkgs.python312Packages.numpy
    pkgs.python312Packages.matplotlib
    pkgs.python312Packages.mysql-connector
  ];

  shellHook = ''
    source ../PythonVenv/bin/activate
  '';
}
