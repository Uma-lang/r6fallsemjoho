// すべての answer クラスを取得
const answers = document.querySelectorAll(".answer");

// それぞれの answer の前の <li> 要素にクリックイベントを追加
answers.forEach((answer) => {
  const listItem = answer.previousElementSibling; // 直前の <li> 要素を取得

  listItem.addEventListener("click", () => {
    // クリック時に回答の表示・非表示を切り替える
    if (answer.style.display === "none") {
      answer.style.display = "block"; // 表示
    } else {
      answer.style.display = "none"; // 非表示
    }
  });
});
