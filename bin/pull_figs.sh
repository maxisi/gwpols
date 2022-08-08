#! /usr/bin/env bash

for f in fig/*.pdf; do
    new_f=${f%.pdf}.png
    magick $f $new_f
    echo "Created ${new_f} from ${f}"
done

mv fig/*.png assets/images/
