import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <section className={styles.intro}>
          <p className={styles.eyebrow}>AI-first banking support</p>
          <h1>Card Emergency Support</h1>
          <p>
            Local frontend foundation for lost-card, suspicious-transaction,
            card information, and human handoff workflows.
          </p>
        </section>
        <section className={styles.statusPanel} aria-label="Foundation status">
          <h2>Phase 0 frontend</h2>
          <p>Next.js, TypeScript strict mode, ESLint, and npm are configured.</p>
        </section>
      </main>
    </div>
  );
}
