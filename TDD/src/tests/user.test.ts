import request from "supertest";
import app from "../src/app";

describe("GET /users", () => {
  it("devrait retourner une liste d'utilisateurs", async () => {
    const res = await request(app).get("/users");
    expect(res.status).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  it("devrait retourner une liste vide si aucun utilisateur n'existe", async () => {
    jest.spyOn(UserService, "getAllUsers").mockResolvedValue([]);
    const res = await request(app).get("/users");
    expect(res.status).toBe(200);
    expect(res.body).toEqual([]);
  });
});
