N = gets.to_i
A = gets.chomp.split(" ").map(&:to_i)

INF = 9_000_000_000

def main
  h = {}
  shortest = INF
  N.times do |i|
    v = A[i]
    if h.has_key?(v)
      l = i - h[v] + 1
      shortest = [shortest, l].min
    end
    h[v] = i
  end

  puts shortest == INF ? -1 : shortest
end

main
