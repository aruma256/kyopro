N, Q = gets.chomp.split.map(&:to_i)

num_to_pos = (0..N).to_a
pos_to_num = (0..N).to_a

Q.times do
  nx = gets.chomp.to_i
  px = num_to_pos[nx]
  py = px < N ? px + 1 : px - 1
  ny = pos_to_num[py]
  num_to_pos[nx], num_to_pos[ny] = py, px
  pos_to_num[px], pos_to_num[py] = ny, nx
end

puts pos_to_num[1..].join(' ')
