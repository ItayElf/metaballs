const drawLine = (ctx: CanvasRenderingContext2D, p1: Point, p2: Point) => {
  ctx.beginPath();
  ctx.strokeStyle = "white";
  ctx.lineWidth = 4;
  ctx.moveTo(p1.x, p1.y);
  ctx.lineTo(p2.x, p2.y);
  ctx.stroke();
};

var circles = getRandomCircles(5);

const mainLoop = (ctx: CanvasRenderingContext2D) => {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
  ctx.fillStyle = "#121212";
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  updateFullCircles(circles);

  ctx.save();

  const lines = getLinesFromFn(getFullFunction(circles));
  for (let i = lines.length - 1; i >= 0; i--) {
    drawLine(ctx, lines[i][0], lines[i][1]);
  }

  //   const gradient = ctx.createLinearGradient(0, 0, WIDTH, 0);
  //   gradient.addColorStop(0, "rgba(255, 0, 0, 1)");
  //   gradient.addColorStop(1, "rgba(0, 255, 0, 1.0)");
  //   ctx.globalCompositeOperation = "destination-out";
  //   ctx.fillStyle = gradient;
  //   ctx.fillRect(0, 0, WIDTH, HEIGHT);

  ctx.restore();
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
  }, 167);
};

main();
