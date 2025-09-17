import yaml


def create_floor_view(floor_name, floor_path, floor_icon, rooms):
    """Generate a floor view with the given floor name and rooms."""
    cards = []

    for room in rooms:
        room_name = room["name"]
        room_area = room["area"]
        room_icon = room["icon"]

        # Add room heading
        cards.append(
            {
                "type": "heading",
                "heading_style": "subtitle",
                "heading": room_name,
                "icon": room_icon,
                "badges": [],
            }
        )

        # Add scene controls
        cards.append(
            {
                "type": "custom:auto-entities",
                "card": {"type": "grid", "columns": 3, "square": False},
                "card_param": "cards",
                "filter": {
                    "include": [
                        {
                            "options": {
                                "type": "custom:bubble-card",
                                "card_type": "button",
                                "button_type": "switch",
                                "show_last_changed": False,
                                "show_state": False,
                                "show_name": False,
                            },
                            "domain": "scene",
                            "area": room_area,
                        }
                    ]
                },
                "sort": {"method": "friendly_name"},
                "show_empty": False,
            }
        )

        # Add cover controls
        cards.append(
            {
                "type": "custom:auto-entities",
                "card": {"type": "grid", "columns": 1, "square": False},
                "card_param": "cards",
                "filter": {
                    "include": [
                        {
                            "options": {
                                "type": "custom:bubble-card",
                                "card_type": "button",
                                "button_type": "slider",
                                "show_last_changed": True,
                                "show_state": True,
                            },
                            "domain": "cover",
                            "area": room_area,
                            "sort": {
                                "method": "friendly_name",
                                "reverse": True,
                            },
                        }
                    ]
                },
                "sort": {"method": "friendly_name"},
                "show_empty": False,
            }
        )

        # Add light controls
        cards.append(
            {
                "type": "custom:auto-entities",
                "card": {"type": "grid", "columns": 1, "square": False},
                "card_param": "cards",
                "filter": {
                    "include": [
                        {
                            "domain": "light",
                            "area": room_area,
                            "options": {
                                "type": "custom:bubble-card",
                                "card_type": "button",
                                "button_type": "slider",
                                "show_last_changed": True,
                                "show_state": True,
                            },
                        }
                    ]
                },
                "sort": {"method": "friendly_name"},
                "show_empty": False,
            }
        )

    return {
        "type": "sections",
        "title": floor_name,
        "path": floor_path,
        "icon": floor_icon,
        "max_columns": 4,
        "sections": [
            {
                "type": "grid",
                "cards": cards,
            }
        ],
    }


def dashboard():
    # Define rooms for the 2F floor
    second_floor_rooms = [
        {"name": "Hall", "area": "second_floor_hall", "icon": "mdi:door"},
        {"name": "Kitchen", "area": "kitchen", "icon": "mdi:chef-hat"},
        {"name": "Living Room", "area": "living_room", "icon": "mdi:sofa"},
        {"name": "Dining Room", "area": "dining_room", "icon": "mdi:table-chair"},
        {"name": "Patio", "area": "patio", "icon": "mdi:table-picnic"},
        {"name": "Office", "area": "office", "icon": "mdi:desk"},
        {"name": "Office Bathroom", "area": "office_bathroom", "icon": "mdi:toilet"},
    ]

    return {
        "views": [
            {
                "title": "Home",
                "type": "sections",
                "max_columns": 4,
                "icon": "mdi:home",
                "sections": [
                    {
                        "type": "grid",
                        "cards": [{"type": "heading", "heading": "New section"}],
                    }
                ],
            },
            create_floor_view("2F", "2f", "mdi:home-floor-2", second_floor_rooms),
        ]
    }


def show(value):
    print(yaml.safe_dump(value))


def main():
    show(dashboard())


if __name__ == "__main__":
    main()
