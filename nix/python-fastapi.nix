{ config, pkgs, ... }:

{
  # Paquetes de sistema que queremos disponibles en la instancia
  environment.systemPackages = with pkgs; [
    python312
    (python312.withPackages (ps: with ps; [
      fastapi
      uvicorn
    ]))
  ];
}
