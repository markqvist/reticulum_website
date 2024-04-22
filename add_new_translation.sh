#!/bin/bash

set -e

origin_directory="./source/"
destiny_directory="./source/"

echo -e "\n"

# Ask the user for the new translation language

read -r -p "Enter the new translation language [es, en, fr, etc]: " new_language

if [[ -z "$new_language" ]]; then
	echo -e "Invalid language code"
	exit 1
fi

echo "Duplicating files for $new_language language"
for file in "$origin_directory"/*; do
	# Took the original files and duplicate them with the new language
	if [[ ! "$file" =~ _ ]]; then
		# Parse name and extesion
		name=$(basename "$file")
		name_without_extension="${name%.*}"
		extension="${name##*.}"
		new_name="${name_without_extension}_${new_language}.${extension}"
		# Duplicate the file
		cp "$file" "$destiny_directory/$new_name"
	fi
done

echo -e "Done, happy translation!"
