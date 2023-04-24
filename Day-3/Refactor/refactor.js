var yourself = {
  memo: {},

  fibonacci: function (n) {
    if (n in this.memo) {
      return this.memo[n];
    } else if (n === 0) {
      return 0;
    } else if (n === 1) {
      return 1;
    } else {
      var result = this.fibonacci(n - 1) + this.fibonacci(n - 2);
      this.memo[n] = result;
      return result;
    }
  },
};
