{
  description = "A basic flake with a shell";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.default = pkgs.mkShell {
        packages = [
			pkgs.python312Packages.filetype
			pkgs.python312Packages.gradio
			pkgs.python312Packages.numpy
			pkgs.python312Packages.psutil
			pkgs.python312Packages.tqdm
			pkgs.python312Packages.scipy
			pkgs.python312Packages.onnx
			pkgs.python312Packages.onnxruntime
			pkgs.python312Packages.opencv4
		];
      };
    });
}
