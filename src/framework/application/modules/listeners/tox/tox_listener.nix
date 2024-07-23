{ pkgs, ... }:

let
  # Define the packages needed to build the Tox listener 
  packages = [
    pkgs.buildPackages.c
    pkgs.buildPackages.c++
    pkgs.zig
    pkgs.cmake
    pkgs.proxychains-ng
    pkgs.lokinet
    pkgs.tor
    pkgs.nym
    pkgs.libtoxcore
    pkgs.libtoxav
    pkgs.libtoxdns
  ];

  # Define the system configuration
  config = {
    # Enable hardened build flags
    security.hardening = {
      enable = true;
      pic = true;
      relro = true;
      bindnow = true;
      fortify = true;
      aslr = true;
      stackProtector = true;
      formatGuard = true;
      formatGuardAll = true;
      formatGuardNoReturn = true;
      formatGuardCheckReturnValue = true;
      formatGuardCheckReturnValueAll = true;
    };
  };
in
{
  # Specify the packages to be installed
  environment.systemPackages = packages;

  # Specify the system configuration
  system = config;
}