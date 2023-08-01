import requests

NOTION_TOKEN = "XXX"  # Find tokens here: https://www.notion.so/my-integrations
DATABASE_ID = "XXX"  # Database ID for your database, like "e7bd26c59e084e0bbaab0045939e7a81" in https://www.notion.so/sarahmakmq-tutorials/e7bd26c59e084e0bbaab0045939e7a81?v=716517a8f10848268ab7a0f8c572429f

title = "Pikachu"
text_content = "Pikachu is a short, chubby rodent Pokémon."

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",  # Check what is the latest version here: https://developers.notion.com/reference/changes-by-version
}


def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    if res.status_code == 200:
        print(f"{res.status_code}: Page created successfully")
    else:
        print(f"{res.status_code}: Error during page creation")
    return res


data = {
    "Name": {
        "id": "title",
        "type": "title",
        "title": [
            {
                "type": "text",
                "text": {"content": title, "link": None},
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default",
                },
                "plain_text": title,
                "href": None,
            }
        ],
    },
}

response = create_page(data)

page_block_id = response.json()["id"]

# Add a text block onto the page


def edit_page(page_block_id, data: dict):
    edit_url = f"https://api.notion.com/v1/blocks/{page_block_id}/children"

    payload = data

    res = requests.patch(edit_url, headers=headers, json=payload)
    if res.status_code == 200:
        print(f"{res.status_code}: Page edited successfully")
    else:
        print(f"{res.status_code}: Error during page editing")
    return res


data = {
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text_content,
                        },
                    }
                ]
            },
        },
    ]
}

edit_page(page_block_id, data)
