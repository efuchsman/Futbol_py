# Futbol in Python

<article>
          <header>
            <h1>
              Statistics
              <small></small>
            </h1>
          </header>
         

<h3 id="game-statistics">Game Statistics</h3>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Return Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">highest_total_score</code></td>
      <td>Highest sum of the winning and losing teams’ scores</td>
      <td>Integer</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">lowest_total_score</code></td>
      <td>Lowest sum of the winning and losing teams’ scores</td>
      <td>Integer</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">percentage_home_wins</code></td>
      <td>Percentage of games that a home team has won (rounded to the nearest 100th)</td>
      <td>Float</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">percentage_visitor_wins</code></td>
      <td>Percentage of games that a visitor has won (rounded to the nearest 100th)</td>
      <td>Float</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">percentage_ties</code></td>
      <td>Percentage of games that has resulted in a tie (rounded to the nearest 100th)</td>
      <td>Float</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">count_of_games_by_season</code></td>
      <td>A hash with season names (e.g. 20122013) as keys and counts of games as values</td>
      <td>Hash</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">average_goals_per_game</code></td>
      <td>Average number of goals scored in a game across all seasons including both home and away goals (rounded to the nearest 100th)</td>
      <td>Float</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">average_goals_by_season</code></td>
      <td>Average number of goals scored in a game organized in a hash with season names (e.g. 20122013) as keys and a float representing the average number of goals in a game for that season as values (rounded to the nearest 100th)</td>
      <td>Hash</td>
    </tr>
  </tbody>
</table>

<h3 id="league-statistics">League Statistics</h3>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Return Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">count_of_teams</code></td>
      <td>Total number of teams in the data.</td>
      <td>Integer</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">best_offense</code></td>
      <td>Name of the team with the highest average number of goals scored per game across all seasons.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">worst_offense</code></td>
      <td>Name of the team with the lowest average number of goals scored per game across all seasons.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">highest_scoring_visitor</code></td>
      <td>Name of the team with the highest average score per game across all seasons when they are away.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">highest_scoring_home_team</code></td>
      <td>Name of the team with the highest average score per game across all seasons when they are home.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">lowest_scoring_visitor</code></td>
      <td>Name of the team with the lowest average score per game across all seasons when they are a visitor.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">lowest_scoring_home_team</code></td>
      <td>Name of the team with the lowest average score per game across all seasons when they are at home.</td>
      <td>String</td>
    </tr>
  </tbody>
</table>

<h3 id="season-statistics">Season Statistics</h3>

<p>These methods each take a season id as an argument and return the values described below.</p>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Return Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">winningest_coach</code></td>
      <td>Name of the Coach with the best win percentage for the season</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">worst_coach</code></td>
      <td>Name of the Coach with the worst win percentage for the season</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">most_accurate_team</code></td>
      <td>Name of the Team with the best ratio of shots to goals for the season</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">least_accurate_team</code></td>
      <td>Name of the Team with the worst ratio of shots to goals for the season</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">most_tackles</code></td>
      <td>Name of the Team with the most tackles in the season</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">fewest_tackles</code></td>
      <td>Name of the Team with the fewest tackles in the season</td>
      <td>String</td>
    </tr>
  </tbody>
</table>

<h3 id="team-statistics">Team Statistics</h3>

<p>Each of the methods below take a team id as an argument. Using that team id, your instance of StatTracker will provide statistics for a specific team.</p>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Return Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">team_info</code></td>
      <td>A hash with key/value pairs for the following attributes: team_id, franchise_id, team_name, abbreviation, and link</td>
      <td>Hash</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">best_season</code></td>
      <td>Season with the highest win percentage for a team.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">worst_season</code></td>
      <td>Season with the lowest win percentage for a team.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">average_win_percentage</code></td>
      <td>Average win percentage of all games for a team.</td>
      <td>Float</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">most_goals_scored</code></td>
      <td>Highest number of goals a particular team has scored in a single game.</td>
      <td>Integer</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">fewest_goals_scored</code></td>
      <td>Lowest numer of goals a particular team has scored in a single game.</td>
      <td>Integer</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">favorite_opponent</code></td>
      <td>Name of the opponent that has the lowest win percentage against the given team.</td>
      <td>String</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">rival</code></td>
      <td>Name of the opponent that has the highest win percentage against the given team.</td>
      <td>String</td>
    </tr>
  </tbody>
</table>

