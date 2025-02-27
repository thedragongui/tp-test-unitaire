import { Request, Response } from "express";
import * as UserService from "../services/userService";

export const getAllUsers = async (req: Request, res: Response) => {
  try {
    const users = await UserService.getAllUsers();
    return res.status(200).json(users);
  } catch (error) {
    return res.status(500).json({ message: "Erreur interne du serveur" });
  }
};

export const getUserById = async (req: Request, res: Response) => {
  try {
    const user = await UserService.getUserById(Number(req.params.id));
    if (!user) {
      return res.status(404).json({ message: "Utilisateur non trouvé" });
    }
    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).json({ message: "Erreur interne du serveur" });
  }
};
