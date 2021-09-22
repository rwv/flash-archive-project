if [[ `git status --porcelain` ]]; then
  # Changes
  echo "Info updated."
  git config --global user.name 'Seedgou'
  git config --global user.email 'i@zczc.cz'
  git commit -am "Update info @ $(date)"
  git push
else
  # No changes
  echo "No Changes."
fi
