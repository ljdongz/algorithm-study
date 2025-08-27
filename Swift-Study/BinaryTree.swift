// MARK: - Array기반 BinaryTree
struct BinaryTreeArray<T: Equatable> {
  private var elements: [T?] = [nil]

  init(rootValue: T) {
    self.elements.append(rootValue)
  }
  
  mutating func insert(_ value: T, at index: Int) {
    expandIfNeeded(index: index)
    elements[index] = value
  }

  private mutating func expandIfNeeded(index: Int) {
    while elements.count <= index {
      elements.append(nil)
    }
  }
}

// MARK: - 순회
extension BinaryTreeArray {
  func preorder(_ index: Int = 1) {
    /// Base Condition
    guard index < elements.count,
          // 완전이진트리가 아닌 경우, 노드 존재 여부 확인
          let node = elements[index]
    else { return }

    print(node)
    preorder(index * 2) // Left Child
    preorder(index * 2 + 1) // Right Child
  }

  func inorder(_ index: Int = 1) {
    /// Base Condition
    guard index < elements.count,
          let node = elements[index]
    else { return }

    inorder(index * 2) // Left Child
    print(node)
    inorder(index * 2 + 1) // Right Child
  }

  func postorder(_ index: Int = 1) {

  }
}