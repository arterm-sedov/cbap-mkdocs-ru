import re
import os
import os.path
import json

KB_ID_MAP_FILE = '.v5mapping.json'
V4_KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map.json'
V5_KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map_v5.json'
DOCS_RU_FOLDER = 'docs/ru'
HYPERLINKS_FILE = os.path.join(DOCS_RU_FOLDER, '.snippets/hyperlinks_mkdocs_to_kb_map.md')


def main():
    
    updateKbIds()

    
def updateKbIds():
    
    v5IdMapping = loadMappingJson(KB_ID_MAP_FILE)
   
    # v4TtitleMapping = loadMappingJson(V4_KB_ID_TO_TITLE_MAP_FILE)
    # v5TtitleMapping = loadMappingJson(V5_KB_ID_TO_TITLE_MAP_FILE)
    
    if not os.path.isdir(DOCS_RU_FOLDER):
        raise FileNotFoundError(f"The directory '{DOCS_RU_FOLDER}' does not exist.")
    
    for root, _, files in os.walk(DOCS_RU_FOLDER):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                updateIdsInFile(file_path, v5IdMapping.get('Articles'))
    
    # for root, _, files in os.walk(DOCS_RU_FOLDER):
    #     for file in files:
    #         if file.endswith(".pages"):
    #             file_path = os.path.join(root, file)
    #             updateIdsInFile(file_path, v5IdMapping.get('Categories'))

    # updateIdsInFile(HYPERLINKS_FILE, v5IdMapping.get('Articles'))
    # updateIdsInFile(HYPERLINKS_FILE, v5IdMapping.get('Categories'))
      
def loadMappingJson(mappingFilename):

    with open(mappingFilename, "r") as mappingJsonFile: 
        mappingJsonFileContent = mappingJsonFile.read()
        mappingJson = json.loads(mappingJsonFileContent) if mappingJsonFileContent else dict()
        return mappingJson

def updateIdsInFile(file_path, mapping):
    
    content = None
    foundMatches = 0
    
    with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for key in mapping:
                targetKbId = mapping.get(key)
                kbIdPattern = re.compile(fr"kbId: {key}", flags=re.MULTILINE)
                foundMatches = foundMatches+1 if kbIdPattern.search(content) else foundMatches
                print(foundMatches)
                content = re.sub(kbIdPattern, fr"kbId: {targetKbId}", content)
    if content and foundMatches:
        with open(file_path, "w+") as file:
            file.write(content)
       

if __name__ == "__main__":
    main()