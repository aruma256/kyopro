H, W = gets.chomp.split.map(&:to_i)

ps = []

(1..H).each do |h|
  s = gets.chomp
  s.each_char.with_index do |c, idx|
    if c == 'o'
      ps << [idx, h]
    end
  end
end

puts (ps[1][0]-ps[0][0]).abs + (ps[1][1]-ps[0][1]).abs
