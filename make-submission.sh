#!/bin/bash

# make-submission.sh
# This script is for pulling together the files needed to submit our
# paper to the arXiv, and stripping out the LaTeX comments to avoid
# and potential embarrassment or secrets.

# USAGE
# Since we send .bbl files to the arXiv, make sure that you've
# successfully compiled the paper first before running this script
#
# If there are files for inclusion that are not in the directory or
# below (i.e. the relative path starts with ..) then we assume it's a
# figure and don't try to preserve the relative path.
# Therefore make sure you're using a \graphicspath{{a/}{b/}} directive
# so that figures can be moved!

# 26 Jan 2015 - Leo C. Stein <leo.stein@gmail.com>
# 16 Dec 2015 - edited by LCS
# 9 Feb 2017 - LCS: also ignore commas in "<use ..." strings.
# 14 Nov 2018 - LCS: Switch from stripcomments.pl to latexpand
# 2 Feb 2019 - LCS: Use mkjobtexmf for list of figures, add flattening of above-dir files

TEMP=`mktemp /tmp/temp.XXXX`

MASTER='polpars'

############################################################

echo ${MASTER}.tex > cp-files
echo ${MASTER}.bbl >> cp-files
# Anything that isn't caught by the code below
cat extra-files >> cp-files

# get list of figures and other files we need
mkjobtexmf --jobname ${MASTER} --cmd-tex pdflatex 2>&1 > /dev/null

grep INPUT ${MASTER}.fls | sed -e '/texmf/d' \
                               -e '/.out/d' \
                               -e '/.aux/d' \
                               -e 's/INPUT //' \
                               -e "/${MASTER}.tex/d" \
                               -e "/${MASTER}.bbl/d" | sort | uniq >> cp-files

############################################################

# make subdirs
grep -o -E '^.+/' cp-files   | sort | uniq > subdirs

mkdir -p submission;
for i in `cat subdirs`; do mkdir -p submission/$i; done;

# copy everything over
rm -f tar-files
for i in `cat cp-files`; do
    j=$i;
    if [[ $i == ..* ]]; then
        j=$(basename $i);
    fi
    cp -af $i submission/$j;
    echo $j >> tar-files
done

############################################################

# Add our ancillary files by hand

############################################################

# strip the tex files
for i in `find submission -name '*.tex'`; do
    latexpand $i --keep-includes --empty-comments -o $TEMP;
    mv $TEMP $i;
done

############################################################

# wrap it up
# The COPYFILE_DISABLE environment variable is for mac os x's version
# of tar, which otherwise would include stupid hidden attribute files.
COPYFILE_DISABLE=true tar -c -C submission -T tar-files -z -f ${MASTER}.tar.gz

############################################################
# # For making submission a little easier: prepare some arXiv metadata into a text file
# echo "Title:" > arXiv-metadata.txt
# grep '\\title' ${MASTER}.tex | head -1 | sed -e 's/\\title{//' -e 's/}//' >> arXiv-metadata.txt
# echo "Authors:" >> arXiv-metadata.txt
# echo "Comments:" >> arXiv-metadata.txt
# echo "" >> arXiv-metadata.txt

############################################################
# Remove sideproducts
rm -r cp-files ${MASTER}.mjt tar-files submission subdirs
