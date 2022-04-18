const drawLine = (ctx: CanvasRenderingContext2D, p1: Point, p2: Point) => {
  ctx.beginPath();
  ctx.moveTo(p1.x, p1.y);
  ctx.lineTo(p2.x, p2.y);
  ctx.stroke();
};

const mainLoop = (ctx: CanvasRenderingContext2D) => {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);

  const fn = (x: number, y: number) => 90 / Math.sqrt(x * x + y * y);
  const fn2 = (x: number, y: number) =>
    70 / Math.sqrt(Math.pow(x - 300, 2) + y * y);
  const lines = getLinesFromFn((x, y) => fn(x, y) + fn2(x, y));
  lines.forEach((l) => {
    drawLine(ctx, l[0], l[1]);
  });
  //   drawLine(ctx, { x: 0.5, y: 0.5 }, { x: 600.3, y: 545.2358 });
};

const main = () => {
  const canvas = document.querySelector("canvas#canvas") as HTMLCanvasElement;
  const ctx = canvas.getContext("2d");
  if (!ctx) {
    console.error("No ctx");
    return;
  }
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  const pixelRatio = window.devicePixelRatio;
  ctx.scale(pixelRatio, pixelRatio);

  setInterval(() => {
    mainLoop(ctx);
  }, 333); // 30 fps
};

main();
