S = gets.chomp

if S != S.downcase && S != S.upcase && S.length == S.chars.uniq.length
  puts 'Yes'
else
  puts 'No'
end
