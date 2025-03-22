# tags: dfs

require "set"

N, M = gets.chomp.split(" ").map(&:to_i)

def main
  @ws = Array.new(N+1) { [] }
  M.times do
    u, v, w = gets.chomp.split(" ").map(&:to_i)
    @ws[u].append([v, w])
    @ws[v].append([u, w])
  end

  @min_w = Float::INFINITY

  def dfs(current_node, current_w, visited)
    if current_node == N
      @min_w = [@min_w, current_w].min
      return
    end

    visited.add(current_node)
    @ws[current_node].each do |next_node, w|
      next if visited.include?(next_node)
      dfs(next_node, current_w ^ w, visited)
    end
    visited.delete(current_node)
  end

  dfs(1, 0, Set.new)

  puts @min_w
end

main
