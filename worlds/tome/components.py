from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:
    from .tome_client import launch_tome_client

    launch(launch_tome_client, name="TOME Client", args=args)


components.append(
    Component(
        "TOME Client",
        func=run_client,
        game_name="Tales of Maj'Eyal",
        component_type=Type.CLIENT,
        supports_uri=False,
    )
)
