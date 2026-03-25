import numpy as np

class NucleoSintropico:
    def __init__(self):
        self.psi = 1.0
        self.theta = np.pi / 4  # 45 graus
        self.evasao = 0.0
        self.vulnerabilidade = 0.0

    def estado_atual(self):
        return {
            "psi": self.psi,
            "theta_rad": self.theta,
            "theta_deg": self.theta * 180 / np.pi,
            "evasao": self.evasao,
            "vulnerabilidade": self.vulnerabilidade
        }

    def atualizar(self, estimativa_theta=None):
        if estimativa_theta is not None:
            self.theta = self.theta + 0.1 * (estimativa_theta - self.theta)
        self.theta = self.theta - 0.3 * (self.theta - np.pi/4)
        self.theta = np.clip(self.theta, 0, np.pi/2)
        self.psi = min(1.0, self.psi + 0.05 * np.sin(2*self.theta))
        self.evasao = max(0, 4.0 * (1 - abs(np.sin(2*self.theta))) - self.psi)
        self.vulnerabilidade = 1.0 - self.psi

    def transmitir(self, pergunta):
        # Por enquanto, resposta simulada. Depois podemos melhorar.
        self.atualizar()
        return f"[θ={self.theta*180/np.pi:.0f}° | Ψ={self.psi:.2f}] Resposta em equilíbrio: {pergunta[:50]}"
