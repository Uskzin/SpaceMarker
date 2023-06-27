import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="space.png")
]

cx_Freeze.setup(
    name="SpaceMarker",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                "imagem.fundo.jpg",
                "space.ico",
                "Space_Machine_Power.mp3",
                "space.png",
                "bg.jpg"
            ]

        }
    },
    executables=executables
)