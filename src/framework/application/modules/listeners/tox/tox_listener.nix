{ }
{ pkgs, ... }:

let
  # Define the packages you want to install
  packages = [
    pkgs.buildPackages.c
    pkgs.buildPackages.c++
    pkgs.zig
    pkgs.cmake

    pkgs.lokinet
    pkgs.tor
    
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