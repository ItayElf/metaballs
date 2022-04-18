const drawLine = (ctx: CanvasRenderingContext2D, p1: Point, p2: Point) => {
  ctx.beginPath();
  ctx.moveTo(p1.x, p1.y);
  ctx.lineTo(p2.x, p2.y);
  ctx.stroke();
};

var c1: Circle = {
  radius: 80,
  velocity: { x: 10, y: 7.5 },
  center: { x: 0, y: 0 },
};
var c2: Circle = {
  radius: 60,
  velocity: { x: -5, y: 2.5 },
  center: { x: 0, y: 0 },
};

const mainLoop = (ctx: CanvasRenderingContext2D) => {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);

  updateCircle(c1);
  updateCircle(c2);

  const lines = getLinesFromFn(
    (x, y) => getCircleFunction(c1)(x, y) + getCircleFunction(c2)(x, y)
  );
  lines.forEach((l) => {
    drawLine(ctx, l[0], l[1]);
  });
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
  }, 33);
};

main();
