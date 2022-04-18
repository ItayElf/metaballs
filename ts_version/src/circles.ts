const getCircleFunction = (c: Circle) => {
  return (x: number, y: number) =>
    c.radius /
    Math.sqrt(Math.pow(x - c.center.x, 2) + Math.pow(y - c.center.y, 2));
};

const updateCircle = (c: Circle) => {
  if (
    c.center.x + c.radius >= WIDTH / 2 ||
    c.center.x - c.radius <= (-1 * WIDTH) / 2
  ) {
    c.velocity.x *= -1;
  }
  if (
    c.center.y + c.radius >= HEIGHT / 2 ||
    c.center.y - c.radius <= (-1 * HEIGHT) / 2
  ) {
    c.velocity.y *= -1;
  }
  c.center.x += c.velocity.x;
  c.center.y += c.velocity.y;
};
